---
title: "iOS - Use fallback paywalls"
description: "Learn how to use fallback paywalls on iOS to ensure seamless user experiences."
metadataTitle: "Using Fallback Paywalls on iOS | Adapty Docs"
---

import Zoom from 'react-medium-image-zoom';
import 'react-medium-image-zoom/dist/styles.css';
import Tabs from '@theme/Tabs'; 
import TabItem from '@theme/TabItem'; 

To use fallback paywalls:

1. Place the fallback JSON file you downloaded in the Adapty Dashboard alongside your app in the user's device.
2. Call the `.setFallbackPaywalls` method. Place this method in your code **before** fetching a paywall, ensuring that the mobile app possesses it when a fallback paywall is required to replace the standard one.

Here's an example of retrieving fallback paywall data from a locally stored JSON file named `ios_fallback.json`.

<Tabs groupId="current-os" queryString>
<TabItem value="swift" label="Swift" default>

```swift showLineNumbers
do {
     if let urlPath = Bundle.main.url(forResource: fileName, withExtension: "json") {
          try await Adapty.setFallbackPaywalls(fileURL: urlPath)
     }
} catch {
    // handle the error
}
```
</TabItem>
<TabItem value="swift-callback" label="Swift-Callback" default>

```swift showLineNumbers
if let url = Bundle.main.url(forResource: "ios_fallback", withExtension: "json") {
     Adapty.setFallbackPaywalls(fileURL: url)
}
```
</TabItem>
</Tabs>


Parameters:

| Parameter   | Description                                                                                                                                                           |
| :---------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **fileURL** | Path to the file with fallback paywalls you [downloaded in the Adapty Dashboard](fallback-paywalls#download-fallback-paywalls-as-a-file-in-the-adapty-dashboard). |