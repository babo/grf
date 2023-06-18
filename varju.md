# Remote access

Here is a quick summary of the action, using ubuntu:jammy as an example

1. As root install sudo, bash and curl on the machine.

    ```apt update && apt install -y sudo bash curl```

2. As you are already there, upgrade the system.

    ```apt upgrade -y```

3. Create a local user for the helper account, from now on we'll call the poor soul as `babo`.

    ```adduser --shell $(which zsh) --disabled-password babo```

4. Add that user to the sudo group.

    ```usermod --append --groups sudo babo```

5. Create an empty ~/.ssh/authorized_keys for that user

    ```mkdir -p ~babo/.ssh && touch ~babo/.ssh/authorized_keys```

6. Ask for a public ssh key, here is mine (note, this is a single line)

    ```ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDCX2cXpK3c2F1UemVLo2UOC1T9DmMYh75JOnYtKVM7NwidXlI3iH2yl9qkissiK/RkDA5V0hJlSZousQ12JCHWr+Snsd5mdZShz86KsI6BDVWGIn0LTfUIQcBhOMwh3XiwHeF4fwTR9CJ4/jIISmCVi5V37uXdACJdeC9vNCaHOT30GJqbUcaGxqZ6IiQ2bIJL/sm96Oc3Qpp98ZabEIgrWnJQOBfyyu2dFSIaqTMiEtSMuZPlFWi4PgD/vuZLDNojk+3w1n5v+EONGoXMKprAdxRGMUoWVmCkZwcT0By4sd3gjzKCuLDoYBGVBs3M3cBQ1X+6QScnLJvVcN2hx3XSU7ZGeu5jT0MDA+qDIECtHFTh3rvUsDAgxI/LmxwcTb2FRtOPMPkXCajDdhMx685FSNjH/KJgcNHmuqF+EocfLHPndjRJ1D/j49tjEJe8IBiXStURqMP93rM3trYH/FV+SKr54W1+PRFiY1ZlZ3eMxGyLYpvqcwNi7Oxm8/9MLoEkRJBthQ12ZxWh2voTYNV6XlrnXuOLkhnwBLBcV+VIe/7Ue9kMcCBp5iN7UijPeaXun+tpjY0wls57leIh3MEtOQsa/sALvuurWMHnkC7qUhYPwuoOW76b1NbHH8I3p9QCDtI+LpTf/nfbETnSHfWkyR2HE9wzz8Aaar+aPWNYJw== attila.babo@gmail.com```

7. Copy that public key into authorized_keys. This command will wait until you copy-paste the key and press Ctrl+D after that:

    ```cat > ~babo/.ssh/authorized_keys```

8. Validate file content:

    ```cat ~babo/.ssh/authorized_keys```

9. Change the file ownership:

    ```chown -R babo:babo ~babo/.ssh```

10. Before securing the SSH server save the original configuration:

    ```cp /etc/sshd/```


https://rgoswami.me/posts/tinyssh-dockerdev-env/
https://github.com/anderspitman/awesome-tunneling

mkdir -p ~/.ssh && chmod 0700 ~/.ssh

ls -ld ~/.ssh
drwx------@ 25 babo  staff  800 May 17 00:29 /Users/babo/.ssh/

sksh-keygen -t ed25519 -f ~/.ssh/id_varju
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/babo/.ssh/id_varju
Your public key has been saved in /Users/babo/.ssh/id_varju.pub
The key fingerprint is:
SHA256:P9mjjE3Mv06IicfUJ5WUUvR63rzEKmFmzud4uOcwSR0 babo@zelota.home
The key's randomart image is:
+--[ED25519 256]--+
|           o+.   |
|          ...o   |
|           .oE.  |
|         . ....  |
|        S o.o..  |
|       + *.@.o.o |
|      . = #+* .oo|
|       . = X+=o .|
|        . ++%= . |
+----[SHA256]-----+

ls -l ~/.ssh/id_varju*
-rw-------  1 babo  staff  464 May 17 00:29 /Users/babo/.ssh/id_varju
-rw-r--r--  1 babo  staff   98 May 17 00:29 /Users/babo/.ssh/id_varju.pub

ssh-add ~/.ssh/id_varju

https://code.visualstudio.com/docs/devcontainers/containers


RUN addgroup -g 1000 grafi && \
    adduser -S -u 1000 -G grafi grafi
