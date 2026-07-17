# -*- coding: utf-8 -*-
"""
第二次及以后更新时用 — 把新的文件从源目录复制过来再推送
用法: python deploy.py
"""

import os
import shutil
import subprocess

SRC = r"D:\002正分子知识库\00_⚪产品分析(功用科普及其他)\000_3功用科普"
DST = r"D:\Personal\Documents\GitHub\gongyong-kepu"

def run(cmd, cwd=DST):
    print(f"> {cmd}")
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding="utf-8")
    if r.stdout: print(r.stdout)
    if r.stderr: print(r.stderr)
    return r.returncode

def main():
    print("=" * 50)
    print(f"复制: {SRC} → {DST}")
    print("=" * 50)

    for item in os.listdir(SRC):
        s = os.path.join(SRC, item)
        d = os.path.join(DST, item)
        # 跳过脚本自身和 git 目录
        if item in ("deploy.py", "push_to_github.py"):
            continue
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
            print(f"  📁 {item}/")
        else:
            shutil.copy2(s, d)
            print(f"  📄 {item}")

    print("\n" + "=" * 50)
    print("Git add + commit + push")
    print("=" * 50)

    run("git add -A")
    run('git commit -m "update: 功用科普知识库更新"')
    code = run("git push")

    if code == 0:
        print("\n✅ 推送成功！")
    else:
        print("\n⚠️  推送失败，尝试拉取合并后重试...")
        run("git pull origin main --allow-unrelated-histories -X ours --no-edit")
        run("git push")

    print("\n🌐 GitHub Pages: https://liuchenyu26131.github.io/gongyong-kepu")

if __name__ == "__main__":
    main()
