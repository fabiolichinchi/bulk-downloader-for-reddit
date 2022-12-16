#!/usr/bin/env python3
# coding=utf-8

import os
import subprocess

import appdirs


class Completion:
    def __init__(self, shell: str):
        self.shell = shell
        self.env = os.environ.copy()
        self.share_dir = appdirs.user_data_dir()
        self.entry_points = ["bdfr"]

    def install(self):
        if self.shell in ("all", "bash"):
            comp_dir = self.share_dir + "/bash-completion/completions/"
            for point in self.entry_points:
                self.env[f"_{point.upper().replace('-', '_')}_COMPLETE"] = "bash_source"
                with open(comp_dir + point, "w") as file:
                    file.write(subprocess.run([point], env=self.env, capture_output=True, text=True).stdout)
                    print(f"Bash completion for {point} written to {comp_dir}{point}")
        if self.shell in ("all", "fish"):
            comp_dir = self.share_dir + "/fish/vendor_completions.d/"
            for point in self.entry_points:
                self.env[f"_{point.upper().replace('-', '_')}_COMPLETE"] = "fish_source"
                with open(comp_dir + point, "w") as file:
                    file.write(subprocess.run([point], env=self.env, capture_output=True, text=True).stdout)
                    print(f"Fish completion for {point} written to {comp_dir}{point}")
        if self.shell in ("all", "zsh"):
            comp_dir = self.share_dir + "/zsh/site-functions/"
            for point in self.entry_points:
                self.env[f"_{point.upper().replace('-', '_')}_COMPLETE"] = "zsh_source"
                with open(comp_dir + point, "w") as file:
                    file.write(subprocess.run([point], env=self.env, capture_output=True, text=True).stdout)
                    print(f"Zsh completion for {point} written to {comp_dir}{point}")

    def uninstall(self):
        if self.shell in ("all", "bash"):
            comp_dir = self.share_dir + "/bash-completion/completions/"
            for point in self.entry_points:
                if os.path.exists(comp_dir + point):
                    os.remove(comp_dir + point)
                    print(f"Bash completion for {point} removed from {comp_dir}{point}")
        if self.shell in ("all", "fish"):
            comp_dir = self.share_dir + "/fish/vendor_completions.d/"
            for point in self.entry_points:
                if os.path.exists(comp_dir + point):
                    os.remove(comp_dir + point)
                    print(f"Fish completion for {point} removed from {comp_dir}{point}")
        if self.shell in ("all", "zsh"):
            comp_dir = self.share_dir + "/zsh/site-functions/"
            for point in self.entry_points:
                if os.path.exists(comp_dir + point):
                    os.remove(comp_dir + point)
                    print(f"Zsh completion for {point} removed from {comp_dir}{point}")
