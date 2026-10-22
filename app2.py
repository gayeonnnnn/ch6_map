import numpy as np
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 앱 제목 설정
st.title("🚇 부산 지하철 역별 이용객 수 지도 분석")

# 2. 호선별 색상 사전 정의 (1호선 주황, 2호선 초록, 3호선 갈색, 4호선 파랑)
COLOR_MAP = {
    "1호선": "#f37321",  # 주황
    "2호선": "#33a845",  # 초록
    "3호선": "#bb9d65",  # 갈색
    "4호선": "#2c8ad8"  # 파랑
}

# 3. CSV 파일 업로드
uploaded_file = st.file_uploader("busan_subway.csv 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # 데이터 읽기
    df = pd.read_csv(uploaded_file)

    # ----------------------------------------------------
    # [기능 1] 호선 필터 (multiselect)
    # ----------------------------------------------------
    st.subheader("🎛️ 호선 선택")

    # 데이터에 존재하는 호선 목록 추출
    available_lines = df['호선'].unique().tolist()

    # 사용자가 선택한 호선 (기본값: 전체 호선 선택)
    selected_lines = st.multiselect(
        "지도에 표시할 호선을 선택하세요:",
        options=available_lines,
        default=available_lines
    )

    # 선택된 호선의 데이터만 필터링
    filtered_df = df[df['호선'].isin(selected_lines)]

    # ----------------------------------------------------
    # [기능 2] 이용객 상위 5개 역 표 표시
    # ----------------------------------------------------
    st.subheader("🏆 선택한 호선의 이용객 상위 5개 역")

    if not filtered_df.empty:
        # 이용객수 기준으로 내림차순 정렬 후 상위 5개 선택
        top5_df = filtered_df.sort_values(by='이용객수', ascending=False).head(5)

        # 순위 정보 추가 및 필요한 열만 정리해서 출력
        top5_display = top5_df[['호선', '역명', '이용객수']].reset_index(drop=True)
        top5_display.index = top5_display.index + 1  # 인덱스를 1위~5위로 변경

        st.dataframe(top5_display)
    else:
        st.warning("선택된 호선이 없습니다.")

    # ----------------------------------------------------
    # [기능 3] folium 지도 표시 (호선별 색상 적용)
    # ----------------------------------------------------
    st.subheader("🗺️ 역별 이용객 수 지도")

    # 부산 중심 좌표 지도 생성
    m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=11)

    # 필터링된 데이터를 순회하며 지도에 마커 추가
    for _, row in filtered_df.iterrows():
        # 원의 면적이 이용객수에 비례하도록 반지름 계산 (제곱근 사용)
        radius_value = np.sqrt(row['이용객수']) * 0.1

        # 호선에 맞는 색상 가져오기 (사전에 없는 호선은 기본 회색)
        line_color = COLOR_MAP.get(row['호선'], "#888888")

        # 원형 마커 생성
        folium.CircleMarker(
            location=[row['위도'], row['경도']],  # 마커 위치
            radius=radius_value,  # 반지름 (이용객수 비례)
            tooltip=f"[{row['호선']}] {row['역명']}",  # 마우스 올렸을 때: 호선 + 역명
            popup=f"{row['역명']}역: {row['이용객수']:,}명",  # 클릭했을 때: 이용객 수
            color=line_color,  # 테두리 색상
            fill=True,
            fill_color=line_color,  # 채우기 색상
            fill_opacity=0.6  # 투명도
        ).add_to(m)

    # Streamlit 화면에 지도 표시
    st_folium(m, width=700, height=500)

else:
    st.info("💡 분석을 시작하려면 CSV 파일을 업로드해주세요.")