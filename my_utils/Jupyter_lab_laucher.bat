@echo off
D:
cd D:\fastbook_project
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\HP\miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\HP\miniconda3\envs\fastai2book'; jupyter-lab "

@REM conda activate fastai2book
@REM jupyter-lab

::https://github.com/zhangjiekui/myNotes/blob/master/Jupyter_lab_launcher.bat
