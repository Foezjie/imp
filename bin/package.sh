#!/bin/bash -xe

VER=$(hg tip | grep -e "changeset:[[:space:]]*[[:digit:]]*:" | grep -o "[[:digit:]]\{1,\}:" | tr -d ":")

if [[ -z $VER ]]; then
    echo "Invalid repo"
    exit
fi

echo "Packaging $VER"

hg clone . /tmp/imp-$VER
sed -i "s/version = .*/version = \"$VER\",/g" /tmp/imp-$VER/setup.py 
HERE=$(pwd)
cd /tmp
tar --exclude=.hg -cvjf $HERE/imp-$VER.tar.bz2 imp-$VER
cd $HERE
rm -rf /tmp/imp-$VER

TDIR=/tmp/impbuild
mkdir -p $TDIR
HOME=$TDIR rpmdev-setuptree
sed -i "s/\%(echo \$HOME)/\/tmp\/impbuild/g" $TDIR/.rpmmacros

mv imp-$VER.tar.bz2 $TDIR/rpmbuild/SOURCES/
cat imp.spec | sed -e "s/^Version:.*/Version:     $VER/g" > $TDIR/rpmbuild/SPECS/imp-$VER.spec

rpmbuild -D "%_topdir $TDIR/rpmbuild" -bb $TDIR/rpmbuild/SPECS/imp-$VER.spec

if [[ "$1" != "" ]]; then
    cp $TDIR/rpmbuild/RPMS/noarch/imp*.rpm $1
    rm -rf $TDIR
fi
