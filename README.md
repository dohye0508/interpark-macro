# 인터파크 취켓팅 매크로 (Interpark Macro)

![Interpark Macro](https://github.com/channnny/interpark-macro/assets/30282985/273fc49e-0619-4610-9cf1-96fe56b790ef)

[![Release](https://img.shields.io/github/v/release/dohye0508/interpark-macro?color=blue&label=Latest%20Release)](https://github.com/dohye0508/interpark-macro/releases)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## About

Python(Tkinter 및 PyAutoGUI) 기반의 인터파크 티켓 예매(취켓팅) 자동화 매크로입니다.  
사용자가 지정한 좌석 영역 내의 좌석(포도알) 색상을 실시간 픽셀 감지하여, 취소 표 발생 시 즉시 좌석 선택 및 결제 단계(좌석선택완료)까지 진행합니다.

---

## 주요 기능

- **GUI 및 실시간 실행 로그**: 프로그램 내 실시간 통합 로그 창을 제공하여 매크로 동작 및 좌표 등록 상황을 한눈에 확인할 수 있습니다.
- **실시간 색상 등록 및 삭제**: `a` 키로 색상을 직관적으로 등록하며, 등록된 색상 목록에서 **더블 클릭**으로 손쉽게 삭제할 수 있습니다.
- **픽셀 기반 고속 탐지**: 지정한 영역 내 RGB 픽셀 값을 실시간 탐지하여 포도알 발생 시 클릭합니다.
- **자동 새로고침 및 결제 단계 연결**: 무작위 딜레이 기반의 새로고침과 좌석선택완료 버튼 자동 클릭을 지원합니다.
- **단축키 정지**: 매크로 동작 중 `;` 키를 눌러 언제든 즉시 정지할 수 있습니다.

---

## 사용 방법

프로그램 실행 후 오른쪽 컨트롤 버튼을 순서대로 눌러 세팅을 진행합니다.

1. **좌석 영역 선택하기**: 버튼 클릭 후 좌석표 좌상단에서 `a`, 우하단에서 `b` 입력.
2. **좌석 등급 선택하기**: 버튼 클릭 후 원하는 좌석 색상 위에서 `a` 입력. (목록 더블 클릭으로 삭제, `c`로 등록 종료)
3. **좌석 새로고침 좌표 가져오기**: 버튼 클릭 후 새로고침 버튼 위에서 `a` 입력.
4. **좌석 선택 완료 좌표 가져오기**: 버튼 클릭 후 좌석선택완료 버튼 위에서 `a` 입력.
5. **매크로 시작 / 중지**: `매크로 시작` 버튼 클릭 (중지는 `;` 키 또는 `매크로 중지` 버튼).

---

## 단축키

| 단축키 | 기능 |
| :---: | :--- |
| **`a`** | 좌표 및 색상 등록 |
| **`b`** | 좌석 영역 우하단 등록 |
| **`c`** | 색상 선택 완료 |
| **`;`** | 매크로 정지 |

---

## 설정 (`main.py`)

```python
NEED_SEAT_CNT = 1  # 예매할 좌석 수
OFFSET = 20        # 클릭 위치 보정 값
ALARM = False      # 성공 알람음 재생 여부
```

---

## 다운로드 및 실행

- **실행 파일**: [Releases](https://github.com/dohye0508/interpark-macro/releases)에서 최신 `.zip` 파일 다운로드.
- **소스코드 실행**:
  ```bash
  pip install pyautogui pillow pygame keyboard
  python main.py
  ```

---

## 라이선스 (License)

[MIT License](LICENSE)
