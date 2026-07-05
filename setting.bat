@echo off
setlocal

REM ==== Git 저장소 루트 확인 ====
for /f "delims=" %%i in ('git rev-parse --show-toplevel 2^>nul') do set "REPO=%%i"
if not defined REPO (
  echo [ERROR] Git 저장소 안에서 실행해 주세요.
  exit /b 1
)

REM ==== 경로 설정 (.github 사용) ====
set "TPL=%REPO%\.github\.gitmessage.txt"
set "HOOKDIR=%REPO%\.githooks"
set "COMMITMSG=%HOOKDIR%\commit-msg"
set "PRECOMMIT=%HOOKDIR%\pre-commit"

echo [INFO] REPO     = %REPO%
echo [INFO] Template = %TPL%
echo [INFO] HooksDir = %HOOKDIR%
echo [INFO] CommitMsg  = %COMMITMSG%
echo [INFO] PreCommit  = %PRECOMMIT%

REM ==== 훅 폴더 보장 ====
if not exist "%HOOKDIR%" mkdir "%HOOKDIR%"

REM ==== 파일 존재 여부 확인 ====
if not exist "%TPL%" (
  echo [ERROR] 템플릿 파일 없음: %TPL%
  echo         .github\.gitmessage.txt 를 먼저 만들어 주세요.
  exit /b 1
)
if not exist "%COMMITMSG%" (
  echo [ERROR] 훅 파일 없음: %COMMITMSG%
  echo         .githooks\commit-msg 를 먼저 만들어 주세요.
  exit /b 1
)

if not exist "%PRECOMMIT%" (
  echo [ERROR] 훅 파일 없음: %PRECOMMIT%
  echo         .githooks\pre-commit 를 먼저 만들어 주세요.
  exit /b 1
)


REM ==== Git 설정(현재 저장소만) ====
git config commit.template ".github/.gitmessage.txt"
git config core.hooksPath .githooks

REM ==== 실행 권한(가능하면 부여) ====
where bash >nul 2>nul
if %ERRORLEVEL%==0 (
  bash -lc "chmod +x .githooks/commit-msg .githooks/pre-commit"
)

echo.
echo [OK] 이 저장소에 커밋 템플릿과 훅을 적용했습니다.
echo  - 템플릿: .github/.gitmessage.txt
echo  - 훅 경로: .githooks
echo.
echo VS Code를 기본 에디터로:  git config core.editor "code -w"
echo.

endlocal