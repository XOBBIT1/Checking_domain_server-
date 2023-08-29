import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function ChartComponent() {
    const [chartData, setChartData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/domain/chart/');
                setChartData(response.data);
            } catch (error) {
                console.error('Error fetching chart data:', error);
            }
        };

        fetchData(); // Инициальный запрос при монтировании компонента

        const intervalId = setInterval(fetchData, 1000); // Обновляем каждую секунду

        return () => {
            clearInterval(intervalId); // Очищаем интервал при размонтировании компонента
        };
    }, []);

    const generateHourlyData = (domainName) => {
        const hourlyData = [];

        for (let hour = 0; hour <= 23; hour++) {
            hourlyData.push({ hour: hour, ping: 0 }); // Инициализируем пинг нулем для каждого часа
        }

        const domainData = chartData.find(data => data.domain_name === domainName);
        if (domainData) {
            domainData.ping_of_domain.forEach(pingData => {
                hourlyData[pingData.hour].ping = pingData.ping;
            });
        }

        return hourlyData;
    };

    return (
        <div>
            <h2>Domain Ping Chart</h2>
            <LineChart width={800} height={400}>
                <XAxis dataKey="hour" />
                <YAxis />
                <CartesianGrid strokeDasharray="3 3" />
                <Tooltip />
                <Legend />
                {chartData.map((data, index) => (
                    <Line
                        key={index}
                        type="monotone"
                        dataKey="ping"
                        name={data.domain_name}
                        data={generateHourlyData(data.domain_name)}
                        stroke={`#${Math.floor(Math.random() * 16777215).toString(16)}`}
                    />
                ))}
            </LineChart>
        </div>
    );
}

export default ChartComponent;
