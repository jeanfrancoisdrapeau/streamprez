# coding=utf-8
import re


def invandraren_trick(data):
    """
    Removes iNVANDRAREN's logo from data:
            )                     )  (      (              (            )
         ( /(           (      ( /(  )\ )   )\ )    (      )\ )      ( /(
     (   )\()) (   (    )\     )\())(()/(  (()/(    )\    (()/( (    )\())
     )\ ((_)\  )\  )\((((_)(  ((_)\  /(_))  /(_))((((_)(   /(_)))\  ((_)\
    ((_) _((_)((_)((_))\ _ )\  _((_)(_))_  (_))   )\ _ )\ (_)) ((_)  _((_)
     (_)| \| |\ \ / / (_)_\(_)| \| | |   \ | _ \  (_)_\(_)| _ \| __|| \| |
     | || .` | \ V /   / _ \  | .` | | |) ||   /   / _ \  |   /| _| | .` |
     |_||_|\_|  \_/   /_/ \_\ |_|\_| |___/ |_|_\  /_/ \_\ |_|_\|___||_|\_|
    """

    # The following un-holy re matches that logo. Sorry for it's ugliness
    invandraren_logo = re.compile(
        "\s*\)\s*\)  \(\s*\(\s*\(\s*\)(.*)(\r*\n)" +
        "\s*\\( \\/\\(\s*\\(\s*\\( \\/\\(  \\)\\\\ \\)   \\)\\\\ \\)\s*\\(" +
        "\s*\\)\\\\ \\)\s*\\( \\/\\((.*)(\r*\n)" +
        "\s*\\(   \\)\\\\\\(\\)\\) \\(   \\(    \\)\\\\     \\)\\\\\\(\\)\\)" +
        "\\(\\(\\)\\/\\(  \\(\\(\\)\\/\\(\s*\\)\\\\\s*\\(\\(\\)\\/\\( \\(\s*" +
        "\\)\\\\\\(\\)\\)(.*)(\r*\n)\s*\\)\\\\ \\(\\(\\_\\)\\\\  \\)\\\\  " +
        "\\)\\\\\\(\\(\\(\\(\\_\\)\\(  \\(\\(\\_\\)\\\\  \\/\\(\\_\\)\\)  " +
        "\\/\\(\\_\\)\\)\\(\\(\\(\\(\\_\\)\\(   \\/\\(\\_\\)\\)\\)\\\\  \\(" +
        "\\(\\_\\)\\\\(.*)(\r*\n)\s*\\(\\(\\_\\) \\_\\(\\(\\_\\)\\(\\(\\_\\)" +
        "\\(\\(\\_\\)\\)\\\\ \\_ \\)\\\\  \\_\\(\\(\\_\\)\\(\\_\\)\\)\\_  " +
        "\\(\\_\\)\\)   \\)\\\\ \\_ \\)\\\\ \\(\\_\\)\\) \\(\\(\\_\\)  \\_" +
        "\\(\\(\\_\\)(.*)(\r*\n)\s*\\(\\_\\)\\| \\\\\\| \\|\\\\ \\\\ \\/ \\/" +
        " \\(\\_\\)\\_\\\\\\(\\_\\)\\| \\\\\\| \\| \\|   \\\\ \\| \\_ \\\\  " +
        "\\(\\_\\)\\_\\\\\\(\\_\\)\\| \\_ \\\\\\| \\_\\_\\|\\| \\\\\\| \\|" +
        "(.*)(\r*\n)\s*\\| \\|\\| \\.\\` \\| \\\\ V \\/   \\/ \\_ \\\\  \\|" +
        " \\.\\` \\| \\| \\|\\) \\|\\|   \\/   \\/ \\_ \\\\  \\|   \\/\\| " +
        "\\_\\| \\| \\.\\` \\|(.*)(\r*\n)\s*\\|\\_\\|\\|\\_\\|\\\\\\_\\|" +
        "  \\\\\\_\\/   \\/\\_\\/ \\\\\\_\\\\ \\|\\_\\|\\\\\\_\\| \\|\\_\\_" +
        "\\_\\/ \\|\\_\\|\\_\\\\  \\/\\_\\/ \\\\\\_\\\\ \\|\\_\\|\\_\\\\\\|" +
        "\\_\\_\\_\\|\\|\\_\\|\\\\\\_\\|(.*)(\r*\n)",
        re.M
    )

    data = re.sub(invandraren_logo, '', data)
    return data