# ArduCopter_app

## チーム説明
コース 3 で組織されたチーム一戸として、コース 2, 3 の課題を行った。コース 2 の課題としては、work/test4EMG_RTL.py を作成した。コース 3 の課題としては、ardupilot/ArduCopter/mode_rtl.cpp, ardupilot/Tools/ardupilotwaf/boards.py を編集、locate.xml を追加した。

## 概要説明
動作している様子を以下の YouTube リンクで示す。

- 想定シーン
    - コプターが指定された複数の Waypoint を　Auto mode で巡行中に、バッテリ電圧が低下し RTL mode でホームに向かうシーン

- 起きうる課題
    - 急激な電圧低下が起きると、コプターはホームまでたどり着けない可能性がある。

- 解決方法
    - ホーム以外に安全に着陸できる「サブホーム」を設定し、「より近いサブホーム」に着陸させる。
    - これにより、急激な電圧降下によって継続した飛行が困難な場合であっても、安全に着陸させる。

## 実際に行ったこと
コース 3 の課題としては、ardupilot/ArduCopter/mode_rtl.cpp, ardupilot/Tools/ardupilotwaf/boards.py を編集、locate.xml を追加し、オリジナルな RTL を改造し、新しいフライトモード（改造 RTL）を作成した。
コース 2 の課題としては、work/test4EMG_RTL.py を作成し、コース 3 で作成したフライトモードのテストを行えるようにした。DroneKit, Pymavlink を使用し、想定シーンの再現を行った。

## Dependencies
SITL, MP を立ち上げた状態で、EMGL.py を実行し、想定シーン（接続 → Arm → 離陸 → WP の設定 → Auto → バッテリ降下 → (改造) RTL）を再現することは可能。
想定シーンの最後の RTL は、オリジナルな ardupilot/ を使用すると RTL モードとなり、コース 3 の課題としてチーム一戸で作成した ardupilot/ を使用すると 改造 RTL となる。

改造 RTL には、以下のパッケージが必要になる。
``` 


