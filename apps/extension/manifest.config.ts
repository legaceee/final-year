import { ManifestV3Export } from "@crxjs/vite-plugin";

const manifest: ManifestV3Export = {
  manifest_version: 3,
  name: "Amazon Review Reader",
  version: "1.0.0",

  content_scripts: [
    {
      matches: [
        "https://www.amazon.in/*",
        "https://www.amazon.com/*"
      ],
      js: ["src/content.ts"]
    }
  ]
};

export default manifest;