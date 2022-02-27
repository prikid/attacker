# Як отримати значення lsb_release якщо у вас Linux Mint


У терміналі вводимо наступне

    cat /etc/upstream-release/lsb-release 

Результат буде виглядати приблизно ось так

    DISTRIB_ID=Ubuntu

    DISTRIB_RELEASE=20.04

    DISTRIB_CODENAME=focal

    DISTRIB_DESCRIPTION="Ubuntu Focal Fossa"

Потрібне нам значення це __focal__ зі строки __DISTRIB_CODENAME=focal__.
У вас воно може відрізнятись