# Увага, кроки описані нижче ви виконуєте на власний ризик, якщо ви не впевнені - краще використайте варіант з python

# Як встановити docker

## Якщо ви використовуєте MacOS

[Інструкція англійською](https://docs.docker.com/desktop/mac/install/)

## Якщо ви використовуєте (Ubuntu,Linux Mint)


[Інструкція англійською](https://docs.docker.com/engine/install/ubuntu/)

Далі дублюються команди з посилання вище для зручності.

    sudo apt-get update

    sudo apt-get install ca-certificates curl gnupg lsb-release

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

Якщо у вас Linux Mint потрібно замінити __$(lsb_release -cs)__  у наступній команді на значення яке можна отримати за цією інструкцією [лінк](/docs/get_lsb_release.md)

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io

## Якщо ви використовуєте Windows

[Інструкція англійською](https://docs.docker.com/desktop/windows/install)


# Як встановити docker-compose

## Ubuntu, Linux Mint

    sudo apt install python3 python3-pip

    pip3 install docker-compose

## Якщо у вас Mac чи Windows
docker-compose повинен встановитись автоматично разом з docker