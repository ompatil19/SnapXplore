import React from "react";
// import "./styles.css";
import * as LR from "@uploadcare/blocks";

LR.registerBlocks(LR);

export default function Uploader() {
    return (
        <div>
            {/* change the pubkey value to your public key from project settings */}
            <lr-config
                ctx-name="my-uploader"
                pubkey="a389d59cb4735c200ff8"
                maxLocalFileSizeBytes={10000000}
                multiple={false}
                imgOnly={true}
                sourceList="local, url, camera, dropbox"
            ></lr-config>
          <lr-file-uploader-regular
            css-src="https://cdn.jsdelivr.net/npm/@uploadcare/blocks@0.30.5/web/lr-file-uploader-regular.min.css"
            ctx-name="my-uploader"
            class="my-config"
          >
          </lr-file-uploader-regular>
        </div>
    );
}
