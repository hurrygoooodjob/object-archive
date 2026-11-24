# Object Archive · 物件字档

Turn text or the outline of a PNG into an arrangement of gemstones, food photographs or emoji. 输入文字或导入 PNG，让珠宝、食品或表情沿轮廓排列。[Open the editor · 在线使用](https://hurrygoooodjob.github.io/object-archive/)

## Try it

1. Open **Jewelry**, **Food & Drink** or **Emoji**. Choose **Text** or **PNG image**.
2. Enter a word such as **Glow** or **回声**, or select an image with a distinct silhouette. Adjust the material, object size and density. Choose a line arrangement or a filled shape.
3. For a sticker, select **Transparent background** below the preview and download a PNG. The checkerboard shows where your background will show through. PNG preserves soft shadows. For a reveal animation, preview it and download a GIF. GIF supports binary transparency.

## 中文使用

1. 打开任一档案袋，在右上角可将 **Language** 切换为 **简体中文**。
2. 输入「回声」或导入轮廓清晰的 PNG。选择素材，再调整沿线或铺满、物件大小和密度。
3. 在预览下方勾选 **透明背景**，点击 **下载 PNG** 即可得到保留柔和投影的贴纸。在 **逐件出现** 中可预览动画并下载透明 GIF。

## Offline and maintenance

Download `index.html` and open it in a modern browser. Fonts, materials and rendering code are embedded. Text, imported images and exports are processed on the device. Changing archive folders keeps the current artwork in the same page session. Emoji appearance follows the device's installed emoji font.

To edit the source as individual files, run these commands with Python 3 from the repository root:

```sh
python3 source.py unpack index.html editor-source
# Edit editor-source/page.html and the relevant JS or CSS files.
python3 source.py pack editor-source rebuilt.html
```

Open `rebuilt.html` to check your changes, then use it as the new `index.html`. Both commands create fresh destinations. Without edits, rebuilding produces a byte-identical copy of the published HTML.

The food photography credits are available in the Food & Drink editor. Attribution, image modifications, font licenses and Unicode data notices are also collected in the repository. [Third-party notices](THIRD-PARTY-NOTICES.txt)
