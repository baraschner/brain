import React from 'react';
import Title from "../user/Title";
import {Legend, Line, LineChart, Tooltip, XAxis, YAxis} from 'recharts';
import moment from 'moment';

class Feelings extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            feelings: null,
            loaded: false
        };
    }

    reformat_data(feelings) {
        let result = []
        feelings.forEach((feeling) => {
                let d = {
                    time: feeling.datetime,
                    hunger: feeling.feelings.hunger,
                    exhaustion: feeling.feelings.exhaustion,
                    happiness: feeling.feelings.happiness,
                    thirst: feeling.feelings.thirst
                }
                result.push(d)
            }
        );
        return result;
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}/all/feelings`)
            .then(response => response.json())
            .then(data => this.setState({feelings: this.reformat_data(data)}));
    }

    render() {
        if (this.state.feelings == null) {
            return `${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/feelings`;
        }

        return (
            <React.Fragment>
                <Title>Feelings</Title>
                <LineChart width={1000} height={300} data={this.state.feelings}>
                    <XAxis dataKey="time" domain={['auto', 'auto']}
                           tickFormatter={(t) => moment(t).format('HH:mm:ss.SSS')}
                           type='number'/>
                    <YAxis/>
                    <Tooltip labelFormatter={(t) => {
                        return moment(t).format('HH:mm:ss.SSS');
                    }} />
                    <Legend/>
                    <Line type="monotone" dataKey="hunger" stroke="#ffcc66" dot={false} />
                    <Line type="monotone" dataKey="thirst" stroke="#82ca11" dot={false}/>
                    <Line type="monotone" dataKey="exhaustion" dot={false}/>
                    <Line type="monotone" dataKey="happiness" stroke="#720025" dot={false}/>
                </LineChart>
            </React.Fragment>
        );
    }
}

export default Feelings;
