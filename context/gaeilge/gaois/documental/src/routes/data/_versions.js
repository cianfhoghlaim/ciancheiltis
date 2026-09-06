import fs from 'fs';

const listVersions = (path) => {
    let versions = [];

    if (!fs.existsSync(path))
        return versions;

    fs.readdirSync(path)
        .filter(item => /(v[0-9a-z.-]+)/.test(item))
        .map(dir => {
            versions.push(dir);
        });

    return versions.sort().reverse();
};

export { listVersions };