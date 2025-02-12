import React, { useState } from 'react';
import { View, Text, TextInput, Button, Alert } from 'react-native';
import YocoSDK from 'react-native-yoco';
import axios from 'axios';

const YOCO_PUBLIC_KEY = "your-public-key";
const PAYMENT_API_URL = "https://your-api-gateway-url/payments";

export default function POS() {
    const [itemId, setItemId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [amount, setAmount] = useState('');

    const processPayment = async () => {
        try {
            const yoco = new YocoSDK({ publicKey: YOCO_PUBLIC_KEY });
            const result = await yoco.showPaymentPopup({
                amountInCents: amount * 100,
                currency: "ZAR"
            });

            if (result.token) {
                const response = await axios.post(PAYMENT_API_URL, {
                    saleId: Date.now().toString(),
                    token: result.token,
                    amount
                });

                Alert.alert("Success", "Payment processed!");
            } else {
                Alert.alert("Error", "Payment failed!");
            }
        } catch (error) {
            Alert.alert("Error", "Payment could not be processed");
        }
    };

    return (
        <View style={{ padding: 20 }}>
            <Text>Item ID:</Text>
            <TextInput value={itemId} onChangeText={setItemId} style={{ borderWidth: 1, padding: 5, marginBottom: 10 }} />
            
            <Text>Quantity:</Text>
            <TextInput value={quantity} onChangeText={setQuantity} keyboardType="numeric" style={{ borderWidth: 1, padding: 5, marginBottom: 10 }} />

            <Text>Amount:</Text>
            <TextInput value={amount} onChangeText={setAmount} keyboardType="numeric" style={{ borderWidth: 1, padding: 5, marginBottom: 10 }} />

            <Button title="Pay with Yoco" onPress={processPayment} />
        </View>
    );
}

