#UMATE

## UMATE is a customized api made to rapidly automate using API

##### Sample for post method
```
{
  "tests": [
    {
      "title": "Open google.com",
      "steps": [
        "SeleniumLibrary.Open Browser    browser=chrome",
        "SeleniumLibrary.Go To    url=https://google.com"
      ]
    }
  ]
}
```