import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder  # Add this line to import LabelEncoder


# Excel 파일 로드
file_path = './Testfile1.xlsx'
df = pd.read_excel(file_path)


print(df.columns)


def find_max_row_diff_and_sort(df):
    # 최대 차이와 해당 인덱스를 저장할 리스트 초기화
    max_diffs = []

    # 모든 열에 대해 반복
    for col in df.columns:
        # 현재 열에 대한 행 간 차이 계산
        diff = df[col].diff().abs()

        # 최대 차이와 해당 인덱스 찾기
        max_diff = diff.max()
        #max_diff = (max_diff <= 0.5).astype(int)
        max_diff_index = diff.idxmax()

        # 리스트에 (열 이름, 최대 차이 인덱스, 최대 차이) 추가
        max_diffs.append((col, max_diff_index, max_diff))

    # DataFrame으로 변환 및 '최대 차이'로 내림차순 정렬
    max_diffs_df = pd.DataFrame(max_diffs, columns=['Column', 'Max Diff Index', 'Max Diff'])
    sorted_max_diffs_df = max_diffs_df.sort_values(by='Max Diff', ascending=False).reset_index(drop=True)
    
    

    return sorted_max_diffs_df


# 'VOLT'가 포함된 열만 대상으로 하는 것을 가정합니다. 다른 열을 대상으로 하려면 조건을 변경하십시오.
volt_cols = [col for col in df.columns if 'VOLT' in col]
df_volt = df[volt_cols]

# 함수 실행 및 결과 출력
sorted_max_diffs_df = find_max_row_diff_and_sort(df_volt)
print(sorted_max_diffs_df)


# 간단한 예시로, 최대 차이값의 상위 10%를 고장으로 가정
#threshold = sorted_max_diffs_df['Max Diff'].quantile(0.9)
#df['Fault'] = (sorted_max_diffs_df['Max Diff'] >= threshold).astype(int)
# −0.05×V N−1
#df['Fault'] = (sorted_max_diffs_df['Max Diff'] > 0.5).astype(int)

# 특성 및 타겟 변수 분리
X = sorted_max_diffs_df[['Max Diff']]  # 여기서는 'max_diff'만 특성으로 사용
print(X)

X['Fault'] = (X['Max Diff'] > 0.5).astype(int)
y = X['Fault']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X[['Max Diff']], y, test_size=0.3, random_state=42)

# 모델 훈련 및 예측
model = GradientBoostingClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 모델 평가
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred))