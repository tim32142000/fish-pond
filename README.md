# Fish Pond

以 Python 製作的互動式魚池模擬，展示魚群移動、隨機投餵與追食行為。

## 功能

- 30 隻魚在池中移動，碰到邊界會轉向；畫面約每 0.2 秒更新一次。
- 每隔約 2–6 秒隨機生成飼料；魚進入感應範圍後朝飼料移動，靠近時吃掉飼料。
- 以網頁即時呈現魚與飼料的位置。

## 技術

- **Python**：魚的移動、邊界與追食模擬。
- **Streamlit**：網頁介面、狀態保存與定時更新。
- **Plotly**：魚池視覺化。

## 本機啟動

```bash
git clone https://github.com/tim32142000/fish-pond.git
cd fish-pond
python -m pip install -r requirements.txt
streamlit run streamlit_app.py
```

執行後在瀏覽器開啟 Streamlit 顯示的本機網址。

## 專案結構

- `simulation.py`：魚、飼料的資料結構與每一步的移動、追食判斷。
- `streamlit_app.py`：魚池畫面、隨機投餵與定時更新。
- `requirements.txt`：執行所需套件。

## 目前限制

- 魚的數量、更新間隔和投餵時間目前由程式常數設定，畫面沒有調整選項。
- 飼料由程式隨機產生，尚無手動投餵功能。
