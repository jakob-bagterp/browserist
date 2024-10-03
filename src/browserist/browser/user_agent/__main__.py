from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .get import get_user_agent


class UserAgentDriverMethods(DriverMethods):
    def __init__(self, browser_driver: BrowserDriver) -> None:
        super().__init__(browser_driver)

    def get(self) -> str:  # type: ignore
        """Get the user agent of the browser.

        Returns:
            The user agent of the browser.

        Example:
            ```python title="" linenums="1"
            user_agent = browser.user_agent.get()
            print(user_agent)
            ```

            How the output could look like in the terminal:

            ```shell title=""
            Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0
            ```
        """

        if self._timeout_should_continue():
            return get_user_agent(self._browser_driver)
