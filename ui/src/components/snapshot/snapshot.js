import React from 'react';
import Typography from '@material-ui/core/Typography';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Feelings from './feelings';
import SnapshotImages from './snapshot_images';
import Pose from './pose';


class Snapshot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            current_snapshot_id: '5ebff198c6431f04cfe8e46b',
            all_snapshots: null,
            loaded: false,
            index: 0
        };
        this.getSnapshotId = this.getSnapshotId.bind(this)
    }

    getSnapshotId() {
        if (this.state.all_snapshots == null) {
            return this.state.current_snapshot_id;
        }

        let snap = this.state.all_snapshots[this.state.index];
        return snap.id;
    }


    render() {
        if (this.state.all_snapshots === []) {
            return 'loading...';
        }
        return (
            <Card>
                <CardContent>
                    <Typography variant='h5'>Snapshot</Typography>
                    <Feelings userId={this.props.userId}/>
                    <SnapshotImages userId={this.props.userId} snapshotId={this.getSnapshotId()}/>
                    <Pose userId={this.props.userId} snapshotId={this.getSnapshotId()}/>
                </CardContent>
                <CardActions>
                    <Button color="secondary" variant="contained" onClick={this.props.close}>Close</Button>
                </CardActions>
            </Card>
        )
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots`)
            .then(response => response.json())
            .then(data => this.setState({all_snapshots: data}));
    }
}

export default Snapshot;
