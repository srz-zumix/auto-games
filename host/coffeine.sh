#!/bin/bash
#
# macOSをスリープさせないスクリプト
# caffeinate コマンドを使用してシステムのスリープを防止します
#
# Author: srz_zumix

set -e

# デフォルト値
DISPLAY_SLEEP=false
DISK_SLEEP=false
IDLE_SLEEP=false
TIMEOUT=""

# 使用方法を表示
show_usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

macOSのスリープを防止するスクリプト

Options:
    -d, --display       ディスプレイのスリープも防止
    -m, --disk          ディスクのスリープも防止
    -i, --idle          アイドルスリープのみ防止
    -t, --timeout SEC   指定秒数後に自動停止
    -h, --help          このヘルプを表示

Examples:
    $(basename "$0")                # システムスリープを防止
    $(basename "$0") -d             # ディスプレイスリープも防止
    $(basename "$0") -t 3600        # 1時間だけスリープを防止
    $(basename "$0") -d -m          # すべてのスリープを防止

Press Ctrl+C to stop
EOF
    exit 0
}

# オプション解析
while [[ $# -gt 0 ]]; do
    case "$1" in
        -d|--display)
            DISPLAY_SLEEP=true
            shift
            ;;
        -m|--disk)
            DISK_SLEEP=true
            shift
            ;;
        -i|--idle)
            IDLE_SLEEP=true
            shift
            ;;
        -t|--timeout)
            TIMEOUT="$2"
            shift 2
            ;;
        -h|--help)
            show_usage
            ;;
        *)
            echo "Error: Unknown option: $1" >&2
            show_usage
            ;;
    esac
done

# コマンドを構築
CMD="caffeinate"

if [ "$DISPLAY_SLEEP" = true ]; then
    CMD="$CMD -d"
fi

if [ "$DISK_SLEEP" = true ]; then
    CMD="$CMD -m"
fi

if [ "$IDLE_SLEEP" = true ]; then
    CMD="$CMD -i"
else
    # デフォルトではシステム全体のスリープを防止
    CMD="$CMD -s"
fi

if [ -n "$TIMEOUT" ]; then
    CMD="$CMD -t $TIMEOUT"
fi

# 終了処理
cleanup() {
    echo ""
    echo "Caffeine stopped."
    exit 0
}

trap cleanup INT TERM

# 実行
echo "Starting caffeine with command: $CMD"
echo "Press Ctrl+C to stop..."
$CMD
