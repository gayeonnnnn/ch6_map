# 🚇 부산 지하철 역별 이용객 수 지도 분석 앱 (Busan Subway Map Analyzer)

Streamlit과 Folium을 활용하여 부산 지하철 역별 이용객 수를 지도 위에 시각화하고 분석하는 웹 애플리케이션입니다. 

---

## 📌 주요 기능 (Features)

1. **데이터 업로드 (`CSV`)**
   - `busan_subway.csv` 파일을 업로드하여 데이터를 불러옵니다.
2. **호선별 필터링 (`Multiselect`)**
   - 1호선~4호선 중 원하는 호선만 선택하여 지도에 표시할 수 있습니다.
3. **인터랙티브 지도 시각화 (`Folium`)**
   - **원 크기**: 이용객 수의 제곱근에 비례하여 마커 반지름이 조절됩니다.
   - **호선별 색상 구분**: 
     - 🟧 1호선: 주황색 (`#f37321`)
     - 🟩 2호선: 초록색 (`#33a845`)
     - 🟫 3호선: 갈색 (`#bb9d65`)
     - 🟦 4호선: 파란색 (`#2c8ad8`)
   - **마우스 호버 (`Tooltip`)**: 역명 표시
   - **마우스 클릭 (`Popup`)**: 이용객 수 표시
4. **상위 5개 역 정보 제공**
   - 선택한 호선 내에서 이용객 수가 가장 많은 상위 5개 역을 순위표로 보여줍니다.

---

## 📁 프로젝트 구조 (Project Structure)

```text
├── app.py              # Streamlit 메인 실행 파일
├── requirements.txt    # 의존성 라이브러리 목록
├── README.md           # 프로젝트 안내 문서
└── busan_subway.csv    # (선택) 부산 지하철 이용객 데이터
```

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language:** Python 3.x
- **Web Framework:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Map Visualization:** Folium, Streamlit-Folium

---

## 🚀 실행 방법 (Getting Started)

### 1. 저장소 클론 (Clone Repository)
```bash
git clone https://github.com/사용자이름/저장소이름.git
cd 저장소이름
```

### 2. 필요 패키지 설치 (Install Dependencies)
```bash
pip install -r requirements.txt
```

### 3. Streamlit 앱 실행 (Run App)
```bash
streamlit run app.py
```

---

## 📊 CSV 데이터 형식 요구사항

업로드하는 CSV 파일은 아래와 같은 열(Column) 이름을 포함해야 합니다:

| 호선 | 역명 | 위도 | 경도 | 이용객수 |
| :--- | :--- | :--- | :--- | :--- |
| 1호선 | 서면 | 35.1577 | 129.0591 | 65000 |
| 2호선 | 해운대 | 35.1637 | 129.1636 | 32000 |

---

💡 *본 프로젝트는 파이썬 데이터 시각화 학습용 프로젝트로 제작되었습니다.*