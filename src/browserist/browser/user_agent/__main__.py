from ...model.browser.base.driver import BrowserDriver
from ...model.driver_methods import DriverMethods
from .get import get_user_agent
from .set import set_user_agent


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

    def set(self, user_agent: str) -> None:
        """Set the `User-Agent` of the browser's request header with a custom value. Note that [not all browsers support changing user agent on the fly](../../settings/user-agent.md#on-the-fly). Alternatively, it's recommended to set the user agent in the [BrowserSettings](../../settings/user-agent.md#for-a-session) when initiating the session.

        Args:
            user_agent (str): The user agent to set.

        Example:
            Basic example:

            ```python title=""
            browser.user_agent.set("MyUserAgent")
            ```

            Or if you want to identify your sessions with a custom value, you can append the existing user agent with your own value:

            ```python title="" linenums="1"
            user_agent = browser.user_agent.get()
            user_agent += " MyUserAgent"
            browser.user_agent.set(user_agent)
            ```
        """

        if self._timeout_should_continue():
            set_user_agent(self._browser_driver, user_agent)
