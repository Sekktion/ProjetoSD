# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pm_pb2 as pm__pb2


class PortalMatriculaStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AdicionaProfessor = channel.unary_unary(
                '/project.PortalMatricula/AdicionaProfessor',
                request_serializer=pm__pb2.DisciplinaPessoa.SerializeToString,
                response_deserializer=pm__pb2.Status.FromString,
                )
        self.RemoveProfessor = channel.unary_unary(
                '/project.PortalMatricula/RemoveProfessor',
                request_serializer=pm__pb2.DisciplinaPessoa.SerializeToString,
                response_deserializer=pm__pb2.Status.FromString,
                )
        self.AdicionaAluno = channel.unary_unary(
                '/project.PortalMatricula/AdicionaAluno',
                request_serializer=pm__pb2.DisciplinaPessoa.SerializeToString,
                response_deserializer=pm__pb2.Status.FromString,
                )
        self.RemoveAluno = channel.unary_unary(
                '/project.PortalMatricula/RemoveAluno',
                request_serializer=pm__pb2.DisciplinaPessoa.SerializeToString,
                response_deserializer=pm__pb2.Status.FromString,
                )
        self.DetalhaDisciplina = channel.unary_unary(
                '/project.PortalMatricula/DetalhaDisciplina',
                request_serializer=pm__pb2.Identificador.SerializeToString,
                response_deserializer=pm__pb2.RelatorioDisciplina.FromString,
                )
        self.ObtemDisciplinasProfessor = channel.unary_stream(
                '/project.PortalMatricula/ObtemDisciplinasProfessor',
                request_serializer=pm__pb2.Identificador.SerializeToString,
                response_deserializer=pm__pb2.RelatorioDisciplina.FromString,
                )
        self.ObtemDisciplinasAluno = channel.unary_stream(
                '/project.PortalMatricula/ObtemDisciplinasAluno',
                request_serializer=pm__pb2.Identificador.SerializeToString,
                response_deserializer=pm__pb2.ResumoDisciplina.FromString,
                )


class PortalMatriculaServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AdicionaProfessor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveProfessor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdicionaAluno(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveAluno(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DetalhaDisciplina(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtemDisciplinasProfessor(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtemDisciplinasAluno(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PortalMatriculaServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AdicionaProfessor': grpc.unary_unary_rpc_method_handler(
                    servicer.AdicionaProfessor,
                    request_deserializer=pm__pb2.DisciplinaPessoa.FromString,
                    response_serializer=pm__pb2.Status.SerializeToString,
            ),
            'RemoveProfessor': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveProfessor,
                    request_deserializer=pm__pb2.DisciplinaPessoa.FromString,
                    response_serializer=pm__pb2.Status.SerializeToString,
            ),
            'AdicionaAluno': grpc.unary_unary_rpc_method_handler(
                    servicer.AdicionaAluno,
                    request_deserializer=pm__pb2.DisciplinaPessoa.FromString,
                    response_serializer=pm__pb2.Status.SerializeToString,
            ),
            'RemoveAluno': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveAluno,
                    request_deserializer=pm__pb2.DisciplinaPessoa.FromString,
                    response_serializer=pm__pb2.Status.SerializeToString,
            ),
            'DetalhaDisciplina': grpc.unary_unary_rpc_method_handler(
                    servicer.DetalhaDisciplina,
                    request_deserializer=pm__pb2.Identificador.FromString,
                    response_serializer=pm__pb2.RelatorioDisciplina.SerializeToString,
            ),
            'ObtemDisciplinasProfessor': grpc.unary_stream_rpc_method_handler(
                    servicer.ObtemDisciplinasProfessor,
                    request_deserializer=pm__pb2.Identificador.FromString,
                    response_serializer=pm__pb2.RelatorioDisciplina.SerializeToString,
            ),
            'ObtemDisciplinasAluno': grpc.unary_stream_rpc_method_handler(
                    servicer.ObtemDisciplinasAluno,
                    request_deserializer=pm__pb2.Identificador.FromString,
                    response_serializer=pm__pb2.ResumoDisciplina.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'project.PortalMatricula', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PortalMatricula(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AdicionaProfessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.PortalMatricula/AdicionaProfessor',
            pm__pb2.DisciplinaPessoa.SerializeToString,
            pm__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveProfessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.PortalMatricula/RemoveProfessor',
            pm__pb2.DisciplinaPessoa.SerializeToString,
            pm__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AdicionaAluno(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.PortalMatricula/AdicionaAluno',
            pm__pb2.DisciplinaPessoa.SerializeToString,
            pm__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveAluno(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.PortalMatricula/RemoveAluno',
            pm__pb2.DisciplinaPessoa.SerializeToString,
            pm__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DetalhaDisciplina(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.PortalMatricula/DetalhaDisciplina',
            pm__pb2.Identificador.SerializeToString,
            pm__pb2.RelatorioDisciplina.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObtemDisciplinasProfessor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/project.PortalMatricula/ObtemDisciplinasProfessor',
            pm__pb2.Identificador.SerializeToString,
            pm__pb2.RelatorioDisciplina.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObtemDisciplinasAluno(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/project.PortalMatricula/ObtemDisciplinasAluno',
            pm__pb2.Identificador.SerializeToString,
            pm__pb2.ResumoDisciplina.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)