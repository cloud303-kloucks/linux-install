import os

def run_command(command):
    print(f"Running command: {command}")
    os.system(command)

def install_app(deb_file):
    command = f"sudo dpkg -i {deb_file}"
    run_command(command=command)

def wget(url, file_name):
    download_cmd = f"wget {url} -O {file_name}"
    run_command(download_cmd)

def main():

    update_command = "sudo apt update && sudo apt upgrade"
    run_command(update_command)

    basic_tools_command = "sudo apt install curl git"
    run_command(basic_tools_command)

    # Install Slack
    slack_url = "https://downloads.slack-edge.com/releases/linux/4.33.73/prod/x64/slack-desktop-4.33.73-amd64.deb"
    slack_deb_file = "slack-desktop-4.33.73-amd64.deb"
    wget(url=slack_url, file_name=slack_deb_file)
    install_app(slack_deb_file)

    # Install vscode
    vscode_url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
    vscode_deb = "vscode.deb"
    wget(url=vscode_url, file_name=vscode_deb)
    install_app(vscode_deb)

    # Install Chrome
    chrome_url = "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb "
    chrome_deb = "google-chrome-stable_current_amd64.deb"
    wget(url=chrome_url, file_name=chrome_deb)
    install_app(chrome_deb)

    zsh_install_command = "sudo apt install zsh"
    run_command(zsh_install_command)

    oh_my_zsh_install_command = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
    run_command(oh_my_zsh_install_command)

    




if __name__ == "__main__":
    main()
