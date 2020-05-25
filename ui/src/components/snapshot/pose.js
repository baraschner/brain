import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";

class Pose extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pose: null,
            loaded: false

        };
    }

    fetch_data() {
        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/pose`)
            .then(response => response.json())
            .then(data => this.setState({pose: data, loaded: true}));

    }

    componentDidMount() {

        this.fetch_data()

    };

    componentDidUpdate(prevProps, prevState) {
        if (prevProps.snapshotId !== this.props.snapshotId) {
            this.fetch_data()
        }
    }


    render() {
        if (!this.state.loaded) {
            return 'loading...';
        }
        return (
            <Card>
                <CardContent><Typography>Pose</Typography></CardContent>
                <CardContent><Typography>Rotation</Typography>
                    ({this.state.pose.translation.x},{this.state.pose.translation.y},{this.state.pose.translation.z})
                </CardContent>
                <CardContent><Typography>Translation</Typography>
                    ({this.state.pose.rotation.x},{this.state.pose.rotation.y},{this.state.pose.rotation.z})
                </CardContent>
            </Card>
        );
    }


}

export default Pose;
