from browserist.model.window.handle import WindowHandle

WINDOW_HANDLE_1_NAME = "1"
WINDOW_HANDLE_1_ID = "CDwindow-8088CB616D7499360039D98453AE91FC"

WINDOW_HANDLE_2_NAME = "2"
WINDOW_HANDLE_2_ID = "CDwindow-89117264372672D3ADAD06DB170AEDF9"

WINDOW_HANDLE_3_NAME = "3"
WINDOW_HANDLE_3_ID = "CDwindow-2587D20E2BC7248E12E4F2F066AAD135"

WINDOW_HANDLE_4_NAME = "4"
WINDOW_HANDLE_4_ID = "CDwindow-5D3DB21221687BEFAC860EF4BD512F42"

WINDOW_HANDLES: list[WindowHandle] = [
    WindowHandle(WINDOW_HANDLE_1_NAME, WINDOW_HANDLE_1_ID),
    WindowHandle(WINDOW_HANDLE_2_NAME, WINDOW_HANDLE_2_ID),
    WindowHandle(WINDOW_HANDLE_3_NAME, WINDOW_HANDLE_3_ID),
    WindowHandle(WINDOW_HANDLE_4_NAME, WINDOW_HANDLE_4_ID),
]
