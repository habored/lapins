# Changelog

!!! note "[0.9.0] - 12-12-2022"

    === "User side modifications"

        - Major | Updated Pyodide version to 21.3
        - Major | Improved console outputs with Rich Text format
        - Major | Centralised Pyodide-MkDocs file architecture in `custom_dir`
        - Major | Improved documentation readability

        --- 

        - Minor | Updated ACE version to 12.5
        - Minor | Updated Terminal version to 2.23

        --- 

        - Minor | IDE : Bug quote in vertical ide
        - Minor | HDR : A regex is now in place and allows for mistakes in HDR tag
        - Minor | HDR : When reloading a page, HDR is now hidden
        - Minor | ERRORLOGGER : when making a mistake, the error was not always correctly displayed

    === "Code quality"

        - Major | Refactored `main.py` to improve robustness and readability
        - Major | CSS : CSS classes are now specialized to avoid scripts-mangling
        - Minor | Simplify remark handling for empty IDE