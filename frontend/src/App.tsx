import { useState, useEffect } from 'react';

import Input from '@mui/material/Input';

let searchInterval: NodeJS.Timeout;

const Container = () => {
    const [search, setSearch] = useState<string>('');

    const searchSongs = async (value: string): Promise<void> => {
        if(!value.length) return;

        const response = await fetch('http://localhost:8989/search/', {
            method: 'POST',
            body: JSON.stringify({ name: value }),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        });

        const result = await response.json();

        console.log(result);
    }

    useEffect(() => {
        clearInterval(searchInterval);

        searchInterval = setTimeout(() => {
            searchSongs(search)
        }, 600)
    }, [ search ])

    return (
        <div>
            <Input
                color="primary"
                onChange={(e) => setSearch(e.target.value)}
            />
        </div>
    )
};

export default Container;
