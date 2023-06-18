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

6. Ask for a public ssh key

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
