import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import axios from 'axios';

const API_URL = "https://your-api-gateway-url/sales";

export default function SalesDashboard() {
    const [salesData, setSalesData] = useState([]);

    useEffect(() => {
        axios.get(API_URL)
            .then(response => setSalesData(response.data.sales))
            .catch(error => console.error("Error fetching sales data", error));
    }, []);

    return (
        <ResponsiveContainer width="100%" height={400}>
            <LineChart data={salesData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="saleId" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="quantity" stroke="#8884d8" />
            </LineChart>
        </ResponsiveContainer>
    );
}

