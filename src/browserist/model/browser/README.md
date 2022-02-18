# About Browser Driver
The browser factory is based on the `BrowserDriver` abstract class that initializes relevant settings for various browsers versions, several abstract methods, and the Selenium web driver. Each sub class to the `BrowserDriver` then implements the specific methods relevant for Chrome, Edge, Firefox, etc.

```mermaid
classDiagram
class BrowserDriver {
    <<abstract>>
    +disable_images()
    +enable_headless()
    +set_page_load_strategy()
}
Chrome --|> BrowserDriver
Edge --|> BrowserDriver
Firefox --|> BrowserDriver
InternetExplorer --|> BrowserDriver
Opera --|> BrowserDriver
Safari --|> BrowserDriver
```
