#!/bin/bash -xe

TDIR=/tmp/build

rm -rf dist
python3 setup.py sdist

rm -rf $TDIR
mkdir -p $TDIR
HOME=$TDIR rpmdev-setuptree
sed -i "s/\%(echo \$HOME)/\/tmp\/build/g" $TDIR/.rpmmacros

cp dist/imp-*.tar.gz $TDIR/rpmbuild/SOURCES/
cp imp.spec $TDIR/rpmbuild/SPECS/imp.spec

rpmbuild -D "%_topdir $TDIR/rpmbuild" -bb $TDIR/rpmbuild/SPECS/imp.spec

if [[ "$1" != "" ]]; then
    cp $TDIR/rpmbuild/RPMS/noarch/*.rpm $1
    rm -rf $TDIR
fi
