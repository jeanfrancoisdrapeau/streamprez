# coding=utf-8
import re


def voxhd_trick(data):
    """
                  `, .``          ``.....,;'++;:`
            ,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#;,`` `  ````.:#@@@+`
         ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+
      `+@@@@@@@@@#  :@@@@@@@@@@@@@@@@@@@@@@@@'@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ;@@@@@@@@@@@,    @@@@@@@@@@@@@@@@@@@@@+    @@@@@@,   @@@@@@@@@@@@@@@@
    @.  #@@@@@@@    #@@@@@@@@@@@@@@@@@@@#      .@@@@@    @@@@;      ,@@@@
    ;    +@@@@@     @@@@@@@@@@+ :@@@@@@`        @@@@@    ,:           `@@
    +     @@@@.    :@@@@@@@@@;    @@@#          @@@@@,                 .@
    @      @@@     @@@@@@@@@@@     #,     '@    @@@@@+         @@@@     @
    @@      @     '@@@@@@@@@@@+          @@@    ;@@@@@         #@@@    `@
    @@@           @@.        @@#       `@@@@     @@@@@    @    .@@     @@
    @@@@         ,@    @@@:   @@#      @@@@@:             @     ;     +@@
    @@@@@        @   ;@@@@@   ;@        .@@@:             @`         +@@@
    @@@@@@.      #   @@@@@+   #           @@@             @#       `@@@@@
    @@@@@@@+     @           .@    '@      @@@    @@@@    @@      #@@@@@@
    @@@@@@@@@. :@@@;       ;@@@    @@@@    @@@:   @@@@    @@.   :@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@    @@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   .@@@@@@@  '@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   +@@@@@@#   #@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ `@@@@@@@+    @@@@
    @@@@@@@@@@@#;      ``...`        @      `.,;+@@@@@@@@#+:``       :@@@
    @@@@@@@@#.                                                       :,.@
    @@@@@@'                                                          :,.@
    @@@,@@            Release.Name.Usually.goes.here-GroupName       :,.@
    """

    vox_logo = re.compile(
        "\s*`, \.``\s*``\.\.\.\.\.\,;'\+\+;:`\s*(.*)(\r*\n)" +
        "\s*,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#;,`` `  ````\.:#@@@\+`(.*)(\r*\n)" +
        "\s*,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\+(.*)(\r*\n)" +
        "\s*`\+@@@@@@@@@#  :@@@@@@@@@@@@@@@@@@@@@@@@'@@@@@@@@@@@@@@@@@@@@@@@@@@@(.*)(\r*\n)" +
        ";@@@@@@@@@@@,    @@@@@@@@@@@@@@@@@@@@@\+    @@@@@@,   @@@@@@@@@@@@@@@@(.*)(\r*\n)" +
        "@\.  #@@@@@@@    #@@@@@@@@@@@@@@@@@@@#      \.@@@@@    @@@@;      ,@@@@(.*)(\r*\n)" +
        ";    \+@@@@@     @@@@@@@@@@\+ :@@@@@@`        @@@@@    ,:           `@@(.*)(\r*\n)" +
        "\+     @@@@\.    :@@@@@@@@@;    @@@#          @@@@@,                 \.@(.*)(\r*\n)" +
        "@      @@@     @@@@@@@@@@@     #,     '@    @@@@@\+         @@@@     @(.*)(\r*\n)" +
        "@@      @     '@@@@@@@@@@@\+          @@@    ;@@@@@         #@@@    `@(.*)(\r*\n)" +
        "@@@           @@\.        @@#       `@@@@     @@@@@    @    \.@@     @@(.*)(\r*\n)" +
        "@@@@         ,@    @@@:   @@#      @@@@@:             @     ;     \+@@(.*)(\r*\n)" +
        "@@@@@        @   ;@@@@@   ;@        .@@@:             @`         \+@@@(.*)(\r*\n)" +
        "@@@@@@\.      #   @@@@@\+   #           @@@             @#       `@@@@@(.*)(\r*\n)" +
        "@@@@@@@\+     @           \.@    '@      @@@    @@@@    @@      #@@@@@@(.*)(\r*\n)" +
        "@@@@@@@@@\. :@@@;       ;@@@    @@@@    @@@:   @@@@    @@\.   :@@@@@@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@    @@@@@@@@@@@@@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   \.@@@@@@@  '@@@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   \+@@@@@@#   #@@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ `@@@@@@@\+    @@@@(.*)(\r*\n)" +
        "@@@@@@@@@@@#;      ``\.\.\.`        @      `\.,;\+@@@@@@@@#\+:``       :@@@(.*)(\r*\n)" +
        "@@@@@@@@#\.                                                       :,\.@(.*)(\r*\n)" +
        "@@@@@@'                                                          :,\.@(.*)(\r*\n)",
        re.M
    )

    data = re.sub(vox_logo, '', data)

    release_name = re.compile("@@@,@@\s*(.*)\s*:,\.@")
    data = re.sub(release_name, r'\1', data)

    return data
