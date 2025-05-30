import { useState } from 'react'; // Import useState hook to manage state
import Chart from "react-apexcharts";

export default function Audience() {
    const [twit, setTwit] = useState("");
    const [series1, setSeries1] = useState([]);

    const [series2, setSeries2] = useState([]);

    const [labels1, setLabels1] = useState([]);

    const [topics, setTopics] = useState([]);
    const [date, setDate] = useState("--:--");

    const chartData1 = {
        type: "pie",
        width: 280,
        height: 280,
        series: series1,
        options: {
            chart: {
                toolbar: {
                    show: false,
                },
            },
            title: {
                show: "",
            },
            dataLabels: {
                enabled: true,
            },
            labels: labels1,
            colors: ["#4CAF50","#FFC107" ,"#2196F3" ,"#FF5722" ,"#9C27B0" ],
            legend: {
                show: false,
            },
        },
    }
    const chartData2 = {
        type: "pie",
        width: 280,
        height: 280,
        series: series2,
        options: {
            chart: {
                toolbar: {
                    show: false,
                },
            },
            title: {
                show: "",
            },
            dataLabels: {
                enabled: true,
            },
            labels: ['0-20', '20-40', '40+'],
            colors: ["#020617", "#ff8f00", "#00897b", "#1e88e5", "#d81b60"],
            legend: {
                show: false,
            },
        },
    }
    

    const handleRunButtonClick = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/getAnalysis', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'userName' : twit }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze the essay');
            }

            try {
                const analysisResults = await response.json();
                console.log(analysisResults);

                setLabels1(analysisResults.top_3_locations);
                setSeries1(analysisResults.location_frequencies);
                setSeries2(analysisResults.age_groups);
                setTopics(analysisResults.hot_topics);
                setDate(analysisResults.recommended_time);

            } catch (error) {
                console.error('Failed to parse response JSON', error);
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="flex gap-x-5 max-w-screen h-screen bg-base-300 shadow-xl p-5">
            <div className="basis-1/3 flex flex-col gap-y-5 max-h-screen">
                <div className="p-5 rounded-[1em] bg-base-100 basis-1/3 shadow-xl max-h-screen">
                    <label className="form-control text-center">    
                        <div className="label">
                            <span className="label-text text-sm">Enter Twitter ID: </span>
                        </div>
                        <div className="flex flex-row gap-x-2">
                            <input type="text" onChange={(e) => {setTwit(e.target.value)}} placeholder="example_123" className="input input-bordered w-full max-w-lg" />
                            <button className="btn btn-primary" onClick={handleRunButtonClick}>Submit</button>
                        </div>
                    </label>
                </div>
                <div className="card bg-base-100 basis-1/2 shadow-xl p-5">
                    <figure>
                        <Chart {...chartData1} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0 mb-0">Countries</h2>
                        <p>Breakdown of your audience, country-wise</p>
                        <div className="card-actions"></div>
                    </div>
                </div>
            </div>
            <div className="card basis-1/3 bg-base-100 shadow-xl p-0">
                <div className="card-body items-center text-center">
                    <h1 className="text-xl font-bold">Trending Topics</h1>
                    <div className="p-0">
                        <table className="table text-lg">
                            <thead>
                            <tr>
                                <th></th>
                                <th>Topics</th>
                            </tr>
                            </thead>
                            <tbody className="pt-0">
                                {topics.map((item, index) => (
                                    <tr key={index}>
                                        <th>#{index + 1}</th>
                                        <td>{item}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            <div className="basis-1/3 flex flex-col gap-y-5">
                <div className="card bg-base-100 basis-2/3 shadow-xl">
                    <figure>
                        <Chart {...chartData2} />
                    </figure>
                    <div className="card-body items-center text-center">
                        <h2 className="card-title pb-0">Age Groups</h2>
                        <p>Breakdown of your audience, age-wise</p>
                        <div className="card-actions"></div>
                    </div>
                </div>
                <div className="p-5 rounded-[1em] bg-zinc-500 basis-1/2 shadow-xl justify-center">
                    <p className="text-lg">Best time to upload: </p>
                    <p className="text-3xl align-middle">{`${date} GMT`}</p>
                </div>
            </div>
        </div>
    );
}















































   
