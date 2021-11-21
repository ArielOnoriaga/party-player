import { useState, useEffect } from 'react';

import Input from '@mui/material/Input';
import Container from '@mui/material/Container';
import ImageListItem from '@mui/material/ImageListItem';

let searchInterval: NodeJS.Timeout;

const SearchContainer = () => {
    const [search, setSearch] = useState<string>('');
    const [tracks, setTracks] = useState<any[]>([]);

    const searchSongs = async (value: string): Promise<void> => {
        if(!value.length) return;

        const response = await fetch('http://localhost:8989/search/', {
            method: 'POST',
            body: JSON.stringify({ name: value }),
            headers: {
                'Content-type': 'application/json',
                'Access-Control-Allow-Origin':'*',
            }
        });

        const result = await response.json();

        setTracks(result.tracks)
    }

    const playSong = async (song: string): Promise<void> => {
        await fetch(`http://localhost:8989/player/play/${song}`, {
            method: 'GET',
            headers: {
                'Access-Control-Allow-Origin':'*',
            }
        });
    }

    useEffect(() => {
        clearInterval(searchInterval);

        searchInterval = setTimeout(() => {
            searchSongs(search)
        }, 600)
    }, [ search ])

    return (
        <Container
            style={{
                display: 'flex',
                flexDirection: 'column'
            }}
        >
            <Input
                color="primary"
                onChange={({ target: { value }}) => setSearch(value)}
            />

            <div
                style={{
                    display: 'grid',
                    gap: '30px',
                    gridTemplateColumns: '160px 160px 160px 160px 160px 160px',
                    marginTop: '20px',
                    maxWidth: '500px',
                }}
            >
                {
                    tracks.map((track, index) =>
                        <button
                            style={{
                                display: 'flex',
                                flexDirection: 'column',
                                padding: '5px',
                            }}
                            key={track.uri}
                            onClick={() => playSong(track.albumUri)}
                        >
                            <ImageListItem key={track.img}>
                                <img
                                    style={{ width: '100%' }}
                                    src={track.img}
                                    alt={track.img}
                                />
                            </ImageListItem>

                            <p style={{ fontSize: '1rem' }}>
                                {track.name}
                            </p>
                        </button>
                    )
                }
            </div>
        </Container>
    )
};

export default SearchContainer;
