import React, { useState } from 'react';

const ClusterComparison: React.FC = () => {
    // Default selected disaster type
    const [disasterType, setDisasterType] = useState('Earthquake');

    // Function to handle changes in the disaster type selection
    const handleDisasterTypeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setDisasterType(event.target.value);
    };

    // Define image paths for multi-cluster and single-cluster for each disaster type
    const imagePathMultiCluster = `/outputs/multi_cluster/multi_cluster_map_${disasterType}.png`;
    const imagePathSingleCluster = `/outputs/single_cluster/single_cluster_map_${disasterType}.png`;

    // Define image paths for elbow curves (multi and single cluster)
    const imagePathMultiElbow = `/outputs/multi_elbow/multi_elbow_curve_${disasterType}.png`;
    const imagePathSingleElbow = `/outputs/single_elbow/single_elbow_curve_${disasterType}.png`;

    return (
        <div className="ClusterComparison pt-24">
            <div className="flex flex-col items-center justify-center space-y-6 p-6">
                <h1 className="text-4xl font-semibold">Compare Clustering Maps</h1>
                <h4 className="text-lg text-center text-gray-700">
                    Choose a disaster type below to compare the clustering maps generated using multi and single algorithms. The left image is 
                    utilizing multialgorithms and the right graph is utilizing single algorithm.
                </h4>

                {/* Options Panel: Dropdown to select disaster type */}
                <div className="mt-6 w-full max-w-2xl">
                    <label htmlFor="disaster-select" className="text-lg text-gray-600">
                        Select Disaster Type:
                    </label>
                    <select
                        id="disaster-select"
                        value={disasterType}
                        onChange={handleDisasterTypeChange}
                        className="p-3 ml-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 text-lg"
                    >
                        <option value="Drought">Drought</option>
                        <option value="Volcanic_activity">Volcanic Activity</option>
                        <option value="Earthquake">Earthquake</option>
                        <option value="Wildfire">Wildfire</option>
                        <option value="Flood">Flood</option>
                        <option value="Storm">Storm</option>
                    </select>
                </div>

                {/* Two images side by side for the comparison (Clustering maps) */}
                <div className="flex space-x-6 mb-6 w-full max-w-4xl">
                    {/* First image (Multi-cluster) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathMultiCluster}
                            alt={`Multi-cluster Map for ${disasterType}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                    {/* Second image (Single-cluster) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathSingleCluster}
                            alt={`Single-cluster Map for ${disasterType}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                </div>

                {/* Two images side by side for the comparison (Elbow curves) */}
                <div className="flex space-x-6 mb-6 w-full max-w-4xl">
                    {/* First image (Multi-cluster Elbow curve) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathMultiElbow}
                            alt={`Multi-cluster Elbow Curve for ${disasterType}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                    {/* Second image (Single-cluster Elbow curve) */}
                    <div className="w-1/2">
                        <img
                            src={imagePathSingleElbow}
                            alt={`Single-cluster Elbow Curve for ${disasterType}`}
                            className="w-full h-auto rounded-lg shadow-xl"
                        />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ClusterComparison;
