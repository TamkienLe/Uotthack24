import React, { useState, useEffect } from 'react';
import { Button, Image, View, Platform } from 'react-native';
import { Camera } from 'expo-camera';
import * as FileSystem from 'expo-file-system';

const App = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [cameraRef, setCameraRef] = useState(null);
  const [imageUri, setImageUri] = useState(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === 'granted');
    })();
  }, []);

  console.log('testing');

  const takePicture = async () => {
    if (cameraRef) {
      const data = await cameraRef.takePictureAsync();
      console.log('data', data);
      setImageUri(data.uri);
      // Save the image after capturing
      saveImage(data.uri);
    }
  };

  const saveImage = async (fileUri) => {
    const fileName = fileUri.split('/').pop();
    // Define a directory path here, for example:
    const directoryPath = FileSystem.documentDirectory + fileName;
    try {
      // Copy the temporary image to a permanent directory
      await FileSystem.moveAsync({
        from: fileUri,
        to: directoryPath,
      });
      console.log('Image saved to:', directoryPath);
    } catch (error) {
      console.error('Error saving the image', error);
    }
  };

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }
  return (
    <View style={{ flex: 1 }}>
      <Camera style={{ flex: 1 }} type={Camera.Constants.Type.back} ref={(ref) => setCameraRef(ref)}>
        <View
          style={{
            flex: 1,
            backgroundColor: 'transparent',
            flexDirection: 'row',
          }}>
          <Button title={"Take Picture"} onPress={() => takePicture()} />
        </View>
      </Camera>
      {imageUri && <Image source={{ uri: imageUri }} style={{ width: 100, height: 100 }} />}
    </View>
  );
};

export default App;  
