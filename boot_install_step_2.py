import os

def run_command(command):
    print(f"Running command: {command}")
    os.system(command)


def main():
    # Install homebrew
    install_homebrew = "/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    run_command(install_homebrew)
    homebrew_path = "(echo; echo 'eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\"') >> /home/$USER/.zprofile "
    run_command(homebrew_path)
    eval_homebrew = "eval \"$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)\""
    run_command(eval_homebrew)

    # Install python3.9 and pip
    install_python39 = "brew install python@3.9"
    run_command(install_python39)
    install_pip = "sudo apt install python3-pip"
    run_command(install_pip)

    # Install AWS CLI
    aws_dl = "curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\""
    run_command(aws_dl)
    unzip = "unzip awscliv2.zip"
    run_command(unzip)
    install_aws_cli = "sudo ./aws/install"
    run_command(install_aws_cli)

    # Install SAM CLI
    install_sam_cli = "brew install aws/tap/aws-sam-cli"
    run_command(install_sam_cli)

    # Install terraform
    install_terraform = "brew tap hashicorp/tap"
    run_command(install_terraform)
    install_tf_version_manager = "brew install tfenv"
    run_command(install_tf_version_manager)

    # Install direnv
    install_direnv = "sudo apt install direnv"
    run_command(install_direnv)
    direnv_path = "(echo; echo 'eval \"$(direnv hook zsh)\"') >> ~/.zshrc "
    run_command(direnv_path)

    # Install saml2
    install_saml = "brew install saml2aws"
    run_command(install_saml)

    # Install Nodejs Version Manager
    install_nvm = "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash"
    run_command(install_nvm)
    chmod_nvm = "chmod ug+x ~/.nvm/nvm.sh"
    run_command(chmod_nvm)
    source_nvm = "source ~/.nvm/nvm.sh"
    run_command(source_nvm)
    install_node = "nvm install --lts"
    run_command(install_node)
    set_node_version = "nvm alias default 18.16.0"
    run_command(set_node_version)

    # Install docker
    get_docker_script = "curl -fsSL https://get.docker.com -o get-docker.sh"
    run_command(get_docker_script)
    install_docker = "sh get-docker.sh"
    run_command(install_docker)



if __name__ == "__main__":
    main()