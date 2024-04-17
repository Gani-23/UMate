import json
import logging
import tempfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from robot import run
from django.shortcuts import render

logger = logging.getLogger(__name__)


def home(request):
    return render(request, "index.html")


@csrf_exempt
def execute_tests(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError as e:
        error_message = f'Error parsing JSON payload: {e}'
        logger.error(error_message)
        return JsonResponse({'error': error_message}, status=400)

    logger.info(f'Parsed payload: {payload}')

    tests = payload.get('tests', [])

    if not tests:
        error_message = 'No tests found in the payload'
        logger.error(error_message)
        return JsonResponse({'error': error_message}, status=400)

    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.robot') as temp_file:
            temp_file.write("*** Settings ***\n")
            temp_file.write("Library    SeleniumLibrary\n")
            temp_file.write("\n")
            temp_file.write("*** Test Cases ***\n")

            for test_case in tests:
                title = test_case.get('title', 'Untitled Test')
                temp_file.write(f"{title}\n")
                steps = test_case.get('steps', [])

                for step in steps:
                    temp_file.write(f"    {step}\n")  # Write the step as-is

                temp_file.write("\n")  # Add a blank line after each test case

        # Print the contents of the temporary file
        with open(temp_file.name, 'r') as f:
            temp_file_content = f.read()
            logger.info(f"Temporary file content:\n{temp_file_content}")

        # Execute the tests using the temporary file
        output = run(temp_file.name)
        logger.info('Test execution completed successfully')

        return JsonResponse({'output': output})

    except Exception as e:
        error_message = f'Error executing tests: {e}'
        logger.error(error_message)
        return JsonResponse({'error': error_message}, status=500)
