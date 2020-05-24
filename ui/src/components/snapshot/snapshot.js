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
            all_snapshots: [],
            loaded: false
        };
        this.update_snapshot_id = this.update_snapshot_id.bind(this)
    }

    update_snapshot_id(time) {
        this.state.all_snapshots.forEach((snapshot) => {
                if (snapshot.time === time) {
                    this.setState({current_snapshot_id: snapshot._id})

                }
            }
        )

    }

    render_snapshot() {
        return (
            <Card>
                <CardContent>
                    <Typography variant='h5'>Snapshot</Typography>
                    <Feelings userId={this.props.userId}  />
                    <SnapshotImages userId={this.props.userId} snapshotId={this.state.current_snapshot_id}/>
                    <Pose userId={this.props.userId} snapshotId={this.state.current_snapshot_id}/>
                </CardContent>
                <CardActions>
                    <Button color="secondary" variant="contained" onClick={this.props.close}>Close</Button>
                </CardActions>
            </Card>
        )
    }

    render() {
        if (this.state.all_snapshots == null) {
            return 'loading';
        }
        return this.render_snapshot()
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots`)
            .then(response => response.json())
            .then(data => this.setState({all_snapshots: data}));
    }
}

export default Snapshot;
