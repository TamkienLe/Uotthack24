// import React, { useState, useEffect } from 'react';
// import { Button, Text, View, ActivityIndicator, Platform, StyleSheet } from 'react-native';
// import { Camera } from 'expo-camera';

// const App = () => {
//   const [hasPermission, setHasPermission] = useState(null);
//   const [cameraRef, setCameraRef] = useState(null);
//   const [isLoading, setIsLoading] = useState(false); // State to manage loading indicator
//   const [showCamera, setShowCamera] = useState(false); // State to show or hide the camera

//   useEffect(() => {
//     (async () => {
//       const { status } = await Camera.requestCameraPermissionsAsync();
//       setHasPermission(status === 'granted');
//     })();
//   }, []);

//     const takePicture = async () => {
//     if (cameraRef) {
//       const options = { base64: true };
//       const data = await cameraRef.takePictureAsync(options);
//       setIsLoading(true); // Show loading immediately after taking the photo
//       const formData = new FormData();      
//       const imageBase64 = data.base64;
  
//       console.log('data', imageBase64);
//       formData.append('files', imageBase64);

//       let res = await fetch(
//         'http://35.208.147.99:80/visionText',
//         {
//           method: 'POST',
//           body: formData,
//           headers: {
//             'Content-Type': 'multipart/form-data;',
//           },
//         }
//       );
//       console.log('res', res);
//       setIsLoading(false);
//     }
//   };

//   if (hasPermission === null) {
//     return <View />;
//   }
//   if (hasPermission === false) {
//     return <Text>No access to camera</Text>;
//   }

//   if (isLoading) {
//     return (
//       <View style={styles.centeredView}>
//         <ActivityIndicator size="large" />
//         <Text>Loading...</Text>
//       </View>
//     );
//   }

//   // Camera view
//   if (showCamera) {
//     return (
//       <Camera
//         style={{ flex: 1 }}
//         type={Camera.Constants.Type.back}
//         autoFocus={Camera.Constants.AutoFocus.on}
//         ref={ref => setCameraRef(ref)}
//       >
//         <View style={styles.cameraView}>
//           <Button title="Take Picture" onPress={takePicture} />
//         </View>
//       </Camera>
//     );
//   }

//   // Initial screen with button to open camera
//   return (
//     <View style={styles.centeredView}>
//       <Button
//         title="Open Camera"
//         onPress={() => setShowCamera(true)}
//       />
//     </View>
//   );
// };

// const styles = StyleSheet.create({
//   centeredView: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//   },
//   cameraView: {
//     flex: 1,
//     backgroundColor: 'transparent',
//     flexDirection: 'row',
//     justifyContent: 'center',
//     // alignItems: 'center',
//     margin: 20,
//   },
// });

// export default App;

import React, { useState, useEffect } from 'react';
import { Button, Text, View, ActivityIndicator, StyleSheet } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const App = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    (async () => {
      const { status } = await ImagePicker.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  const takePicture = async () => {
    let result = await ImagePicker.launchCameraAsync({
      allowsEditing: false,
      aspect: [4, 3],
      quality: 1,
      base64: true,
    });

    if (!result.cancelled) {
      setIsLoading(true);
      const formData = new FormData();
      const imageBase64 = result.assets[0].base64;

      console.log(result.assets[0].base64);
      formData.append('files', imageBase64);

      let res = await fetch(
        'http://35.208.147.99:80/visionText',
        {
          method: 'POST',
          body: formData,
          headers: {
            'Content-Type': 'multipart/form-data;',
          },
        }
      );
      console.log('res', res);
      setIsLoading(false);
    }

    }

  if (hasPermission === null) {
    return <View />;
  }

  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  if (isLoading) {
    return (
      <View style={styles.centeredView}>
        <ActivityIndicator size="large" />
        <Text>Loading...</Text>
      </View>
    );
  }

  // Initial screen with button to open camera
  return (
    <View style={styles.centeredView}>
      <Button
        title="Take a Picture"
        onPress={takePicture}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default App;
