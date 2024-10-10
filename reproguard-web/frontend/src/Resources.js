import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Resources = () => {
    const [resources, setResources] = useState([]);

    useEffect(() => {
        const fetchResources = async () => {
            const response = await api.get('/resources');
            setResources(response.data);
        };
        fetchResources();
    }, []);

    return (
        <div>
            <h2>Educational Resources</h2>
            <ul>
                {resources.map(resource => (
                    <li key={resource.id}>{resource.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default Resources;