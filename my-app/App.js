import React, { useState, useEffect } from 'react';
import { Image, Text, View, ActivityIndicator, StyleSheet, TouchableOpacity} from 'react-native';
import * as ImagePicker from 'expo-image-picker';

const App = () => {
  const [hasPermission, setHasPermission] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [responseData, setResponseData] = useState(null);

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

    if (!result.canceled) {
      setIsLoading(true);
      const formData = new FormData();
      const imageBase64 = result.assets[0].base64;

      // console.log(result.assets[0].base64);
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

      res.json().then((data) => {
        setResponseData(data);
        // console.log(res.json());
      }).finally(() => {
        setIsLoading(false);
      });
    }
  }

  // Function to format and display the data
  const formatData = (data) => {
  let displayData = data['Brand_Description'] ? data['Brand_Description'] + '\n\n' : ''; // Include 'Brand_Description' if it exists

  // Iterate over the data and include only positive values, except for 'Brand_Description'
    Object.keys(data).forEach(key => {
    if (key !== 'Brand_Description' && data[key] > 0 && data[key] != true) {
      if (key == "Total_Score") {
        displayData += `${key.replace(/_/g, ' ')}: ${data[key]}\n\n`;
      } else if (key == "Material_Footprint" || key == "Shipping_Footprint") {
        displayData += `${key.replace(/_/g, ' ')}: ${data[key]}kg of CO2\n`;
      } else if (key == "Water_Usage") {
        displayData += `${key.replace(/_/g, ' ')}: ${data[key]}L\n`;
      } else if (key != "Brand_Score") {
        displayData += `${key.replace(/_/g, ' ')}: ${data[key]}L\n`;
      } else {
        displayData += `${key.replace(/_/g, ' ')}: ${data[key]}\n`;
      }
    }
  })
  return displayData.trim(); // Remove last newline character
}

  if (hasPermission === null) {
    return <View />;
  }

  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  if (isLoading) {
    return (
      <View style={styles.loadingCenter}>
        <ActivityIndicator size="large" />
        <Text style={styles.loadingText}>Loading...</Text>
      </View>
    );
  }

  // Initial screen with button to open camera
return (
    <View style={styles.centeredView}>
      <Text style={styles.sustainTitle}> sustain.</Text>
      <TouchableOpacity onPress={takePicture}>
        <Image
          source={require('./assets/croppedNoBG.png')}
          style={styles.buttonImage}
        />
      </TouchableOpacity>
      <Text style={styles.sustainTopText}> sustaining the environment</Text>
      <Text style={styles.sustainBottomText}> through everyday wear</Text>
      {responseData && (
        <Text style={styles.dataText}>
          {formatData(responseData)}
        </Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  centeredView: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#063923',
  },
  buttonImage: {
    width: 150,
    height: 150
  },
  loadingCenter: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#063923',
    color: '#94B84A',
  },
  loadingText: {
    fontSize: 36,
    color: '#94B84A',
  },
  sustainTitle: {
    fontSize: 36,
    color: '#94B84A',
    paddingBottom: 24
  },
  sustainTopText: {
    fontSize: 24,
    color: '#94B84A',
    paddingTop: 24
  },
  sustainBottomText: {
    fontSize: 24,
    color: '#94B84A',
  },
  dataText: {
    marginTop: 20,
    textAlign: 'center',
    color: '#94B84A',
    width: '100%', // Ensure the text aligns left and spans the full width
  },
});

export default App;