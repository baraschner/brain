import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";

class Pose extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pose: null,
        };
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/pose`)
            .then(response => response.json())
            .then(data => this.setState({pose: data}));
    };

    render() {
        if (this.state.pose == null) {
            return `${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/feelings`
        }
        return (
            <Box width={1 / 2}>
                <Card>
                    <CardContent><Typography>Pose</Typography></CardContent>
                    <CardContent><Typography>Rotation</Typography>
                        ({this.state.pose.translation.x},{this.state.pose.translation.y},{this.state.pose.translation.z})
                    </CardContent>
                    <CardContent><Typography>Translation</Typography>
                        ({this.state.pose.rotation.x},{this.state.pose.rotation.y},{this.state.pose.rotation.z})
                    </CardContent>
                </Card>
            </Box>
        );
    }


}

export default Pose;
