# ArduCopter_app  

## 概要説明
動作している様子を以下の動画で示す。（画質は 1080p で閲覧してください。）  
test1 https://drive.google.com/file/d/17dWtHmriebNcA_99P5_JRD5-ukOf8Itx/view?usp=sharing  
test2 https://drive.google.com/file/d/13lo30dfXUXxoS2tb99sdFGbT_4WVDsvX/view?usp=share_link  

- 想定シーン
    - コプターが指定された Waypoint を Auto mode で巡行中に、バッテリ電圧が低下し RTL mode でホームに向かうシーン

- 起きうる課題
    - 急激な電圧低下が起きると、コプターはホームまでたどり着けない可能性がある。

- 解決方法
    - ホーム以外に安全に着陸できる「サブホーム」を設定し、「より近いサブホーム」に着陸させる。
    - これにより、急激な電圧降下によって継続した飛行が困難な場合であっても、安全に着陸させる。

## 実際に行ったこと
コース 3 の課題として実装したコードは、https://github.com/1014ksg/ardupilot.git リポジトリの feat/EMGL ブランチにある。  
具体的には、ardupilot/ArduCopter/mode_rtl.cpp, ardupilot/Tools/ardupilotwaf/boards.py を編集、locate.xml を追加した。  
オリジナルな RTL を改造し、新しいフライトモード（改造 RTL）を作成した。 

コース 2 の課題として実装したコードは、https://github.com/1014ksg/ArduCopter_app.git リポジトリの master ブランチ、work/test4EMG_RTL.py にある。  
コース 3 で作成したフライトモードのテストを行えるようにした。DroneKit, Pymavlink を使用し、想定シーンの再現を行った。    

## Usage
SITL, MP を立ち上げた状態で、test4EMG_RTL.py を実行し、想定シーン（接続 → Arm → 離陸 → WP の設定 → Auto → バッテリ降下 → (改造) RTL）を再現することが可能。  
想定シーンの最後の RTL は、https://github.com/1014ksg/ardupilot.git リポジトリの master ブランチ を使用すると RTL モードとなり、コース 3 の課題としてチーム一戸で作成した https://github.com/1014ksg/ardupilot.git リポジトリの feat/EMGL ブランチ を使用すると 改造 RTL モードとなる。  

## Dependencies
改造 RTL には、以下のパッケージが必要になる。  
``` git clone  https://github.com/1014ksg/ardupilot.git ```（ feat/EMGL ブランチ）  
``` sudo apt install librapidxml-dev -y ```



