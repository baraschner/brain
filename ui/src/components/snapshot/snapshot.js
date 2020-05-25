import moment from "moment";

import React from 'react';

import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';

import PlayCircleFilledIcon from '@material-ui/icons/PlayCircleFilled';
import StopIcon from '@material-ui/icons/Stop';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';

import Feelings from './feelings';
import SnapshotImages from './snapshot_images';
import Pose from './pose';
import FastForwardIcon from '@material-ui/icons/FastForward';
import FastRewindIcon from '@material-ui/icons/FastRewind';


class Snapshot extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            all_snapshots: null,
            loaded: false,
            index: 0,
            speed_index: 0
        };
        this.speeds = [1, 1.2, 1.4, 1.6, 1.8, 2]
        this.getSnapshotId = this.getSnapshotId.bind(this)
        this.setInterval = this.setInterval.bind(this)
        this.unsetInterval = this.unsetInterval.bind(this)
        this.fast = this.fast.bind(this)
        this.slow = this.slow.bind(this)
    }

    getSnapshotId() {
        if (this.state.all_snapshots == null) {
            return this.state.current_snapshot_id;
        }

        return this.state.all_snapshots[this.state.index].id;
    }

    updateSnapshotId(add) {
        if (this.state.index == null) {
            return;
        }

        this.setState(prevState => ({
            index: (prevState.index + add + prevState.all_snapshots.length) % prevState.all_snapshots.length
        }));

    }

    fast() {
        this.setState(prevState => ({
            speed_index: Math.min(prevState.speed_index + 1, this.speeds.length)
        }))
        this.setInterval()
    }

    slow() {
        this.setState(prevState => ({
            speed_index: Math.max(prevState.speed_index - 1, 0)
        }))
        this.setInterval()
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    setInterval() {
        this.unsetInterval()
        this.interval = setInterval(
            () => this.updateSnapshotId(1),
            1000 / this.speeds[this.state.speed_index]); //once every 1 second

    }

    unsetInterval() {
        clearInterval(this.interval)
    }

    render() {
        if (!this.state.loaded) {
            return 'loading...';
        }

        return (
            <Card>
                <CardContent>
                    <Typography variant='h5'>Snapshot</Typography>
                    <Feelings userId={this.props.userId}/>
                    <SnapshotImages userId={this.props.userId} snapshotId={this.getSnapshotId()}/>
                    <Pose userId={this.props.userId} snapshotId={this.getSnapshotId()}/>
                    <Typography color="textSecondary">
                        {moment(parseInt(this.state.all_snapshots[this.state.index].datetime)).format('HH:mm:ss.SSS')}
                    </Typography>

                   </CardContent>


                    <CardActions>
                        <IconButton onClick={this.updateSnapshotId.bind(this, -1)}>
                            <ChevronLeftIcon/>
                        </IconButton>
                        <IconButton onClick={this.updateSnapshotId.bind(this, 1)}>
                            <ChevronRightIcon/>
                        </IconButton>
                        <IconButton onClick={this.setInterval}>
                            <PlayCircleFilledIcon/>
                        </IconButton>
                        <IconButton onClick={this.slow}>
                            <FastRewindIcon/>
                        </IconButton>
                        <IconButton onClick={this.fast}>
                            <FastForwardIcon/>
                        </IconButton>

                        <IconButton onClick={this.unsetInterval}>
                            <StopIcon/>
                        </IconButton>


                        <Button color="secondary" variant="contained" onClick={this.props.close}>Close</Button>

                    </CardActions>

            </Card>
    );
    }

    componentDidMount() {

        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots`)
            .then(response => response.json())
            .then(data => {
                     {
                        this.setState({
                                all_snapshots: data,
                                loaded: true
                            }
                        )
                    }
                }
            )
    }

    }

    export default Snapshot;
