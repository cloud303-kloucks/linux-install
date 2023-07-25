import os

def run_command(command):
    print(f"Running command: {command}")
    os.system(command)

def main():

    update_command = "sudo apt update && sudo apt upgrade"
    run_command(update_command)

    zsh_install_command = "sudo apt install zsh"
    run_command(zsh_install_command)

    oh_my_zsh_install_command = 'sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
    run_command(oh_my_zsh_install_command)

    url = "https://downloads.slack-edge.com/releases/linux/4.33.73/prod/x64/slack-desktop-4.33.73-amd64.deb"
    slack_deb_file = "slack-desktop-4.33.73-amd64.deb"
    
    download_command = f"wget {url} -O {slack_deb_file}"
    run_command(download_command)
    
    install_command = f"sudo dpkg -i {slack_deb_file}"
    run_command(install_command)

if __name__ == "__main__":
    main()
