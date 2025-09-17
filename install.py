#!/data/data/com.termux/files/usr/bin/bash
# ===========================================
#  Termux Banner Installer
# ===========================================

BANNER_PATH="$HOME/banner.txt"

echo -e "\n[+] Menginstall Termux Banner..."

# Copy banner.txt ke $HOME
cp banner.txt $BANNER_PATH

# Tambah ke .bashrc kalau belum ada
if ! grep -q "cat ~/banner.txt" $HOME/.bashrc; then
    echo "cat ~/banner.txt" >> $HOME/.bashrc
    echo "[+] Banner ditambahkan ke ~/.bashrc"
else
    echo "[*] Banner sudah ada di ~/.bashrc"
fi

# Kalau pakai zsh (opsional)
if [ -f "$HOME/.zshrc" ]; then
    if ! grep -q "cat ~/banner.txt" $HOME/.zshrc; then
        echo "cat ~/banner.txt" >> $HOME/.zshrc
        echo "[+] Banner ditambahkan ke ~/.zshrc"
    fi
fi

echo -e "\n[✔] Install selesai! Silakan restart Termux.\n"
